*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set password_confirmation  kalle123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  p
    Set Password  something2
    Set password_confirmation  something2
    Click Button  Register
    Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Set Username  poika
    Set Password  hi
    Set password_confirmation  hi
    Click Button  Register
    Register Should Fail With Message  Too short password

Register With Valid Username And Invalid Password
    Set Username  poika
    Set Password  minaolenpoika
    Set password_confirmation  minaolenpoika
    Click Button  Register
    Register Should Fail With Message  Put number in password


Register With Nonmatching Password And Password Confirmation
    Set Username  poika
    Set Password  minaolenpoika2
    Set password_confirmation  minaolenpoika
    Click Button  Register
    Register Should Fail With Message  unmatching passwords

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set password_confirmation  kalle123
    Click Button  Register
    Register Should Succeed
    Go to Register page
    Set Username  kalle
    Set Password  kalle1234
    Set password_confirmation  kalle1234
    Click Button  Register
    Register Should Fail With Message  User with username kalle already exists


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register page

Register Should Succeed
    Welcome page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}


Set Password_confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}