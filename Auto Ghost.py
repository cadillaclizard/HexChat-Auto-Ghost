import hexchat

__module_name__ = "Auto Ghost"
__module_version__ = "0.1"
__module_description__ = "Automatic ghostig"


def ghost(word, word_eol, userdata):
    nickname = hexchat.get_prefs("irc_nick1")
    password = hexchat.get_info("nickserv")

    hexchat.command("nickserv ghost %s %s" % (nickname, password))
    hexchat.command("nick %s" % nickname)
    hexchat.command("nickserv identify %s" % password)
    return hexchat.EAT_NONE


hexchat.hook_server("433", ghost, priority=hexchat.PRI_HIGHEST)
