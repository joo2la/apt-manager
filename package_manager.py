import os
pack_list = []
print("APT-MANAGER Successfully Launched")
while True:
	com = input(">").lower()
	if com in {"create", "create pack-list", "cr"}:
		print("Enter the names of the packages, separated by a space")
		repo = input(">")
		pack_list = repo.split(' ')

	elif com in {"add", "add to pack-list"}:
		print("Enter the names of the packages, separated by a space that you want to add")
		repo = input(">")
		pack_list = pack_list + repo.split(' ')

	elif com in {"checklist", "cl", "list", "pack"}:
		if len(pack_list) != 0:
			for i in range(len(pack_list)):
				print(f'[{i}]:[{pack_list[i]}]')
		else:
			print("No packages!!")

	elif com in {"del-pack", "dp", "del"}:
		print("Enter the batch number in the list")
		number = int(input(">"))
		if number <= -1:
			pack_list = []
			print("Package List Successfully Cleared!")
		else:
			try:
				pack_list.pop(number)
				print("Package Successfully Deleted!")
			except IndexError:
				print("There is no package with this number!")

	elif com in {"setup", "install", "inst"}:
		if len(pack_list) != 0:
			for i in range(len(pack_list)):
				os.system(f'sudo apt install {pack_list[i]} -y')
			print("Successfully!")
		else:
			print("No packages!")

	elif com in {"remove", "rm-pack", "rm"}:
		if len(pack_list) != 0:
			for i in range(len(pack_list)):
				os.system(f'sudo apt remove {pack_list[i]} -y')
			os.system("sudo apt autoremove")
			print("Successfully!")
		else:
			print("No packages!")

	elif com in {"help", "commands"}:
		print("create, create pack-list, cr - create your package list")
		print("add, add to pack-list - add your package to list")
		print("del-pack, dp, del - delete your package from list")
		print("checklist, cl, list, pack - show list")
		print("setup, install, inst - install all package from list")
		print("remove, rm-pack, rm - uninstall all package from list + autoremove")