import os
import shutil
import random



# Define deletion paths
del_world = r"C:\Users\ripar\Desktop\Minecraft Server\world"
del_nether = r"C:\Users\ripar\Desktop\Minecraft Server\world_nether"
del_end = r"C:\Users\ripar\Desktop\Minecraft Server\world_the_end"

# If the old world folders exist, delete them
if os.path.exists(del_world):
    shutil.rmtree(del_world)
if os.path.exists(del_nether):
    shutil.rmtree(del_nether)
if os.path.exists(del_end):
    shutil.rmtree(del_end)

# Get input for seed (random if a custom seed isn't wanted)
newSeed = input("Enter seed (Type \"NONE\" if you want a random seed): ")
if newSeed == "NONE" or newSeed == "None" or newSeed == "none":
    random.seed()
    newSeed = random.randint(1, 3999999999)
    print(newSeed)

# Server.properties formatted text
serverDefaultText = """#Minecraft server properties
#Sat Aug 22 12:10:11 EDT 2020
spawn-protection=16
max-tick-time=60000
query.port=25565
generator-settings=
sync-chunk-writes=true
force-gamemode=false
allow-nether=true
enforce-whitelist=false
gamemode=survival
broadcast-console-to-ops=true
enable-query=false
player-idle-timeout=0
difficulty=easy
spawn-monsters=true
broadcast-rcon-to-ops=true
op-permission-level=4
pvp=true
entity-broadcast-range-percentage=100
snooper-enabled=true
level-type=default
hardcore=false
enable-status=true
enable-command-block=true
max-players=20
network-compression-threshold=256
resource-pack-sha1=
max-world-size=29999984
function-permission-level=2
rcon.port=25575
server-port=25565
debug=false
server-ip=192.168.1.144
spawn-npcs=true
allow-flight=false
level-name=world
view-distance=10
resource-pack=
spawn-animals=true
white-list=false
rcon.password=
generate-structures=true
online-mode=true
max-build-height=256
level-seed={}
prevent-proxy-connections=false
use-native-transport=true
enable-jmx-monitoring=false
motd=A Minecraft Server
enable-rcon=false
""".format(newSeed)

# Remove the old property file
propertiesPath = r"C:\Users\ripar\Desktop\Minecraft Server\server.properties"
os.remove(propertiesPath)

# Creates temp txt file for prop
newFilePath = r"C:\Users\ripar\Desktop\testWrite.txt"
newFile = open(newFilePath, 'w')

# Writes new data and saves/closes file
newFile.write(serverDefaultText)
newFile.close()

# Copy the prop.txt into server folder as a properties file
shutil.copyfile(newFilePath, propertiesPath)

# Delete old prop.txt
os.remove(newFilePath)