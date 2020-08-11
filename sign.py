from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,0,"第一行","第二行","第三行","第四行")