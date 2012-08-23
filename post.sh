#! /bin/bash


#
#    Peter Novotnak :: Binarysprocket LLC :: 2012
#






name="post.sh"
usage="usage: $name [projects folder] [url]"
correct_usage="starting post operations!.."

project_path=''
project_name=''


# Exit if the argument passed is not zero, and print an error message
con() {
  if [ "$1" == "0" ]
  then
    echo -ne ""
  else
    echo "
    
    ERROR! $2
    
    "
    exit
  fi
}


# Make sure the project actually exists
find_project() {
  if [ -d "$1" ]
    then
      return 0
    else
      return 1
  fi
}


find_name() {
  echo "Importing :: $(basename "$1")"
  return 0
}







# Run the functions!
if [ -z "$1" ] || [ -z "$2" ]
  then
    echo $usage
  else
    project_path="$1"
    activecollab_url="$2"
    find_project "$project_path"
    con "$?" "Couldn't find the project path specified!"
    project_name="$(find_name "$project_path")"
    curl -d "submitted=submitted" \
      --data-urlencode "project[name]=$project_name" \
      --data-urlencode "project[leader_id]=1" \
      "$activecollab_url/activecollab/public/api.php?path_info=projects&token=2-7UzlPY4InJ24x0yTOeetI6p61ezXYCTT26yPX83v"
fi # Have a nice day!
