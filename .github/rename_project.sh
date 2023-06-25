#!/usr/bin/env bash
while getopts a:n:u:d: flag
do
    case "${flag}" in
        a) author=${OPTARG};;
        n) name=${OPTARG};;
        u) urlname=${OPTARG};;
        d) description=${OPTARG};;
    esac
done

echo "Author: $author";
echo "Project Name: $name";
echo "Project URL name: $urlname";
echo "Description: $description";

echo "Renaming project..."

original_author="keshavdv"
original_name="dometic_cfx3"
original_urlname="dometic-cfx3"
original_description="Awesome dometic_cfx3 created by keshavdv"
# for filename in $(find . -name "*.*") 
for filename in $(git ls-files) 
do
    sed -i "s/$original_author/$author/g" $filename
    sed -i "s/$original_name/$name/g" $filename
    sed -i "s/$original_urlname/$urlname/g" $filename
    sed -i "s/$original_description/$description/g" $filename
    echo "Renamed $filename"
done

mv dometic_cfx3 $name

# This command runs only once on GHA!
rm -rf .github/template.yml
