def buildApp() {
    echo 'building the application...'
}

def testApp() {
    echo 'Testing the application...'
}

def deployApp() {
    echo 'Deploy the application...'
    echo "deploying version: ${params.VERSION}"
}

def inputMessage() {
    echo "Deploying to ${params.ENV}"
}

return this