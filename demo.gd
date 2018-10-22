extends Panel

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	var tree = $Tree
	var root = tree.create_item()
	tree.set_hide_root(true)
	var child1 = tree.create_item(root)
	var child2 = tree.create_item(root)
	var subchild1 = tree.create_item(child1)
	subchild1.set_text(0, "Subchild1")



func _on_Button_button_down():
	$FileDialog.popup()
