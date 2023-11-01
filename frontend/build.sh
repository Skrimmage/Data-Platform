# shell

# run the build command to build the static pages
npm run build

# copy the 
cp CNAME ./build/CNAME
cp _redirects ./build/_redirects

# TODO copy over the default evidence files
# cp ./replace/icon.svg ./build/icon.svg 

# ./build/icon.svg
# ./build/favicon.ico
# ./build/icon-192.png
# ./build/icon-512.png
# ./build/apple-touch-icon.png

# replace ./build/_app/immutable/assets/wordmark-gray-800.3686622c.png
#name=$(find ./build/_app/immutable/assets -name "wordmark*" )
#cp ./replace/wordmark.png $name



