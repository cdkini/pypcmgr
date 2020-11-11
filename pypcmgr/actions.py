import os


def run(path, flags):
    """TODO: Add method description!

    Args:
        path (str):
        flags (argparse.Namespace):

    """
    if flags.config and flags.default:
        pass  # Should raise error that flags cannot be both used
    elif flags.config:
        config(path, flags)
    elif flags.default:
        config(path, flags)
    else:
        pass


def config(path, flags):
    """TODO: Add method description!

    Args:
        path (str):
        flags (argparse.Namespace):

    """
    if os.path.exists(".pre-commit-config.yaml"):
        print(f"Config file already found in {path}")
        confirmation = input("Are you sure you want to reset your settings? (Y/N): ")
        if confirmation.lower() != "y":
            print("Terminating config command")
            return
    os.mknod(".pre-commit-config.yaml")


def hook(path, flags):
    """TODO: Add method description!

    Args:
        path (str):
        flags (argparse.Namespace):

    """
    print("hook not yet implemened")


def ls(path, flags):
    """TODO: Add method description!

    Args:
        path (str):
        flags (argparse.Namespace):

    """
    print("ls not yet implemented!")


def reset(path, flags):
    """TODO: Add method description!

    Args:
        path (str):
        flags (argparse.Namespace):

    """
    confirmation = input("Are you sure you want to reset your settings? (Y/N): ")
    if confirmation.lower() != "y":
        print("Terminating reset command")
        return

    delete_config = False if flags.hook and not flags.config else True
    if delete_config:
        if not os.path.exists(path + ".pypcmgrconfig"):
            raise ValueError(f".pypcmgrconfig not found in {path}")
        os.remove(path + ".pypcmgrconfig")
        print(f"Deleted .pypcmgrconfig in {path}")

    delete_hooks = False if flags.config and not flags.hook else True
    if delete_hooks:
        if not os.path.exists(path + ".pre-commit-config.yaml"):
            raise ValueError(f".pre-commit-config.yaml not found in {path}")
        os.remove(path + ".pre-commit-config.yaml")
        print("Deleted .pre-commit-config.yaml")
