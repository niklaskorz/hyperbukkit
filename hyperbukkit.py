import org.bukkit as bukkit
import org.yaml.snakeyaml as snakeyaml
import os
import threading
import bottle
import routes

config_defaults = """host: 0.0.0.0
port: 8080
debug: false
quiet: true
"""

log = bukkit.Bukkit.getServer().getLogger()
data_path = "plugins/" + info.getName()
config_path = data_path + "/config.yml"
webapp = bottle.Bottle()

@hook.enable
def onenable():
    log = pyplugin.getLogger()
    yaml = snakeyaml.Yaml()

    if not os.path.exists(data_path):
        log.info("Creating data directory... ({})".format(data_path))
        os.makedirs(data_path)
    if not os.path.exists(config_path):
        log.info("Creating config file... ({})".format(config_path))
        with open(config_path, "w") as config_file:
            config_file.write(config_defaults)

    with open(config_path, "r") as config_file:
        global config
        config = yaml.load(config_file)

    log.info("Initializing routes...")
    routes.init(bottle, webapp)

    log.info("Starting HTTP server on {}:{}...".format(config["host"], config["port"]))
    bottle.debug(config["debug"])
    threading.Thread(target=lambda: webapp.run(host=config["host"], port=config["port"], quiet=config["quiet"])).start()
