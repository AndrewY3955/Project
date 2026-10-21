#!/usr/bin/env sh
set -eu

PROFILE_FILE="${HOME}/.bashrc"
case "${SHELL:-}" in
    */zsh) PROFILE_FILE="${HOME}/.zshrc" ;;
esac
BEGIN_MARKER="# BEGIN PROJECT_DASHBOARD_RUN_MACRO"
END_MARKER="# END PROJECT_DASHBOARD_RUN_MACRO"
TEMP_PROFILE="${PROFILE_FILE}.tmp.$$"

touch "$PROFILE_FILE"
awk -v begin="$BEGIN_MARKER" -v end="$END_MARKER" '
    $0 == begin { skip = 1; next }
    $0 == end { skip = 0; next }
    !skip { print }
' "$PROFILE_FILE" > "$TEMP_PROFILE"
cat >> "$TEMP_PROFILE" <<'EOF'

# BEGIN PROJECT_DASHBOARD_RUN_MACRO
run() {
    (
        directory=$PWD
        while [ "$directory" != "/" ]; do
            if [ -f "$directory/run.sh" ]; then
                sh "$directory/run.sh" "$@"
                return $?
            fi
            directory=$(dirname "$directory")
        done
        if [ -f /run.sh ]; then
            sh /run.sh "$@"
            return $?
        fi
        printf '%s\n' "Could not find run.sh. Change to the cloned project directory and run 'run' again." >&2
        return 1
    )
}
# END PROJECT_DASHBOARD_RUN_MACRO
EOF
mv "$TEMP_PROFILE" "$PROFILE_FILE"
printf "Installed the portable 'run' command in %s.\n" "$PROFILE_FILE"
printf "Open a new terminal, change to a cloned project, and run: run\n"
