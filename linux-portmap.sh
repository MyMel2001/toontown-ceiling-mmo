export IP=$(hostname  -I | cut -f1 -d' ')
upnpc -a $IP 1913 1913 tcp