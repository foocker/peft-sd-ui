import launch

if not launch.is_installed("peft"):
    try:
        launch.run_pip("install peft", "requirements for peft")
    except:
        print("Can't install peft. Please follow the readme to install manually")