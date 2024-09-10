import roblox

# Access the local player and their mouse
local_player = roblox.game.Players.LocalPlayer
mouse = local_player.GetMouse()

# Initialize running variable
running = False

# Function to get the tool
def get_tool():
    for child in script.Parent:GetChildren():
        if child.ClassName == "Tool":
            return child
    return None

# Connect the KeyDown event handler
mouse.KeyDown:connect(function(key):
    key = key.lower()
    if string.byte(key) == 48:
        running = True
        key_connection = mouse.KeyUp:connect(function(key):
            if string.byte(key) == 48:
                running = False
            end
        end)
        for i in range(1, 6):
            roblox.game.Workspace.CurrentCamera.FieldOfView = 70 + (i * 2)
            roblox.wait()
        roblox.game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = 35
        while running:
            roblox.wait()
        key_connection:disconnect()
        roblox.game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = 16
        for i in range(1, 6):
            roblox.game.Workspace.CurrentCamera.FieldOfView = 80 - (i * 2)
            roblox.wait()
    end
end)