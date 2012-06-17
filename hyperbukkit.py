import org.bukkit as bukkit
import org.yaml.snakeyaml as snakeyaml

log = bukkit.Bukkit.getServer().getLogger()

@hook.enable
def onenable():
    log = pyplugin.getLogger()
