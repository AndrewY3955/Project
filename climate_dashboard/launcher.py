"""Prepare reviewed dashboard data and start the local browser app."""

import argparse
import urllib.error
import urllib.request
import webbrowser

from climate_dashboard.dashboard import ROOT, serve


def _dashboard_is_running(url: str) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=1) as response:
            return response.status == 200 and b"Semiconductor Climate Data Dashboard" in response.read()
    except (urllib.error.URLError, TimeoutError):
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare data and run the local climate dashboard.")
    parser.add_argument("--port", type=int, default=8765, help="Local HTTP port (default: 8765)")
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Do not open the dashboard in the default browser.",
    )
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")

    reviewed_dir = ROOT / "data" / "processed" / "reviewed"
    input_file = ROOT / "data" / "intake" / "observations_template.csv"

    from climate_dashboard.pipeline import run_pipeline

    result = run_pipeline(input_file=input_file, output_dir=reviewed_dir)
    print(
        f"Reviewed data: {result['status']} "
        f"({result['row_count']} records, {result['error_count']} errors, "
        f"{result['warning_count']} warnings)"
    )

    from climate_dashboard.adversarial import create_adversarial_copy

    changes = create_adversarial_copy(
        trusted_file=reviewed_dir / "trusted_data.csv",
        output_dir=reviewed_dir,
    )
    print(
        f"Created separate adversarial dataset and logged {len(changes)} "
        "intentional manipulation events."
    )
    print("This is a controlled simulation, not a real attack.")

    from climate_dashboard.powerbi_export import build_powerbi_pack

    powerbi_result = build_powerbi_pack(
        reviewed_dir=reviewed_dir,
        output_dir=ROOT / "data" / "powerbi",
    )
    print(
        f"Power BI import pack: {powerbi_result['status']} "
        f"({powerbi_result['table_count']} tables; "
        f"trusted hash {'MATCH' if powerbi_result['manifest_match'] else 'MISMATCH'})"
    )

    url = f"http://127.0.0.1:{args.port}/"
    if _dashboard_is_running(url):
        print(f"Dashboard is already running at {url}; refreshed data is available.")
        if not args.no_browser and not webbrowser.open(url):
            print("Could not open a browser automatically; open the URL above manually.")
        return

    serve(args.port, open_browser=not args.no_browser)


if __name__ == "__main__":
    main()
