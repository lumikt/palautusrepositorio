*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Reset Application
    Go To Register Page
    Set Username  testi
    Set Password    testi123
    Repeat Password    testi123
    Click Button    Register
    Title Should Be    Welcome to Ohtu Application!

Login After Successful Registration
    Go To Register Page
    Set Username  testi
    Set Password    testi123
    Repeat Password    testi123
    Click Button    Register
    Go To Main Page
    Click Button    Logout
    Go To Login Page
    Set Username    testi
    Set Password    testi123
    Click Button    Login
    Title Should Be    Ohtu Application main page

Register With Too Short Username And Valid Password
    Reset Application
    Go To Register Page
    Set Username  a
    Set Password    testi123
    Repeat Password    testi123
    Click Button    Register
    Page Should Contain    Username is too short

Login After Failed Registration
    Reset Application
    Go To Register Page
    Set Username  testi
    Set Password    a
    Repeat Password    a
    Click Button    Register
    Go To Login Page
    Set Username    testi
    Set Password    a
    Click Button    Login
    Page Should Contain    Invalid username or password
    

Register With Valid Username And Too Short Password
    Reset Application
    Go To Register Page
    Set Username  testi
    Set Password    a1
    Repeat Password    a1
    Click Button    Register
    Page Should Contain    Password doesn't match requirements


Register With Valid Username And Invalid Password
    Reset Application
    Go To Register Page
    Set Username  testi
    Set Password    testitesti
    Repeat Password    testitesti
    Click Button    Register
    Page Should Contain    Password doesn't match requirements


Register With Nonmatching Password And Password Confirmation
    Reset Application
    Go To Register Page
    Set Username  testi
    Set Password    testi123
    Repeat Password    123testi
    Click Button    Register
    Page Should Contain    Passwords don't match

Register With Username That Is Already In Use
    Reset Application
    Create User   testi  testi123
    Go To Register Page
    Set Username  testi
    Set Password    testi123
    Repeat Password    testi123
    Click Button    Register
    Page Should Contain    Username unavailable


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Repeat Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
