### install 
` apt install tmux | yum install tmux | brew install tmux `


### new window 
tmux new
tmux new -s xxx  

### disconnect
tmux detach
ctrl + b + d 

### into to old session
tmux a 
tmux a -t xxx 

### exit tmux 
tmux kill-session -t xxx 
tmux kill-server   

### view all session
tmux list-session
tmux ls

### open session list
ctrl + b + s

### open window-session list 
ctrl + b + w

### System Command
Crtl + b + ? : help  
Ctrl + b + d : disconnect  
Crtl + b + D : select disconnect session    
Ctrl + b + z : Hang session  
Ctrl + b + r : reload session  
Ctrl + b + s : view session list for select  
Ctrl + b + : : into to cmd,eg: ls  
Ctrl + b + [ : inrto copy mode  
Ctrl + b + ] : parse copy text  
Ctrl + b + ~ : list cache info  

### Window Command
Ctrl + b + c : new window  
Ctrl + b + & : exit window  
Ctrl + b + 0~9: switch window   
Ctrl + b + p : switch previous  
Ctrl + b + n : switch next  
Ctrl + b + w : open window list for switch  
Ctrl + b + , : rename window name  
Ctrl + b + . : change window number  
Ctrl + b + f : fast locate window number 

### Pane Command
Ctrl + b + " : UP and DOWN Segmentation Pane  
Ctrl + b + % : Left and Right Segmentation Pane  
Ctrl + b + x : Close Current Pane  
Ctrl + b + z : Maximum Current Pane   
Ctrl + b + ! : Move Current Pane to new window  
Ctrl + b + ; : Switch Last Used Pane  
Ctrl + b + q : Display Pandl Number  
Ctrl + b + { : Forward Replacement Current Panel  
Ctrl + b + } : Backward Relacement Current Panel  
Ctrl + b + Ctrl + o : Rotate Current All Pane  
Ctrl + b + o : select next panel  
Ctrl + b + 方向键: Move Cursor Switch Panel  
Ctrl + b + 空格键: self panel switch cycle  
Ctrl + b + Alt + 方向键: 以五个单元调整面板边缘
Ctrl + b + Ctrl + 方向键: 以一个单元为单位调整当前面板边缘
Ctrl + b + t : Display Clock

### TMUX Config 
vim ~/.tmux.conf 
set -g prefix C-a	// 设置绑定前缀
unbind C-b			// 解除绑定
bind C-a send-prefix   // 绑定Ctrl + a 为新的指令前缀

set-option -g prefix2 `  // 设置第二个指令前缀 ` 键

### END
