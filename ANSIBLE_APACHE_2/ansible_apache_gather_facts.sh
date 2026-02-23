echo '----'
echo "IPV4 ADDRESS"
ip addr | grep "inet "
echo '----'
# show ansible config file
echo "ANSIBLE CONFIG FILE"
cat ansible.cfg
echo
# Check ansible version
echo "ANSIBLE VERSION"
ansible --version
echo '----'
# show ansible inventory file (hosts)
echo "ANSIBLE INVENTORY"
cat hosts
echo '----'
# Verify status of Apache no local serverl
echo "VERIFY IF APACHE2 IS ACTIVE"
sudo systemctl status apache2
echo '----'
# VéFify TCP Ports
echo "VERIFY APACHE TCP PORTS"
cat /etc/apache2/ports.conf | grep Listen
echo '----'
# Verify available Apache sites
