def buldApp() {
     echo 'build the application'
     echo "build with mentioned version "
}
def testApp() {
     echo 'test the application'
}
def deployApp() {
     echo 'deploye the the application on server'
     echo "doploy the version ${params.VERSION}"
}
return this
