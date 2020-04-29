



export SECRET_KEY="59044ec228c7ddc3172f037a9ef288c2ebc709a137e95083"
export DEBUG_VALUE="True"

for file in ~/.{bash_prompt,aliases,private}; do
    [ -r "$file"] && [ -f "$file"] && source "$file";
done;
unset file;