# shell

export EVIDENCE_DATABASE=csv

# run the build command to build the static pages
npm run build

#echo "replacing DNS"
#cp CNAME ./build/CNAME
#cp _redirects ./build/_redirects
# Note: I removed this section by adding those files to the static folder. 
# If those ever get added to anything other than the root level directory, important to add this back.

echo "replacing icons"
cp ./replace/icon.svg ./build/icon.svg 
cp ./replace/favicon.ico ./build/favicon.ico 
cp ./replace/icon-192.png ./build/icon-192.png
cp ./replace/icon-512.png ./build/icon-512.png
cp ./replace/apple-touch-icon.png ./build/apple-touch-icon.png

# replace ./build/_app/immutable/assets/wordmark-gray-800.3686622c.png
name=$(find ./build/_app/immutable/assets -name "wordmark*" )
cp ./replace/wordmark.png $name

echo "done"

