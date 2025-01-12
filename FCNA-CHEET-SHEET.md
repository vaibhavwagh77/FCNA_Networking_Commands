# FCNM Cheat Sheet

## Overview
This cheat sheet is designed to provide a concise and accessible reference for understanding the fundamentals of networking and configuration, including IPv4/IPv6 addressing, subnetting, VLANs, and routing. Ideal for professionals and students working with network setups.

## 1. Switch and Router Basics

- **Switch**: Connects devices in a LAN.
- **Router**: Connects devices between two LANs.
- **Intranet**: Internal LAN operations.
- **Internet**: WAN operations.

## 2. IPv4 Addressing

- **Address Structure**: 32-bit (4 bytes); Total: 2^32 (4.3 billion).
- **Classes**:
  - **Class A**: 1-126; Subnet Mask: /8; Networks: 2^7 = 128; Hosts: 2^24 = 16.7M.
  - **Class B**: 128-191; Subnet Mask: /16; Networks: 2^14 = 16,384; Hosts: 2^16 = 65,536.
  - **Class C**: 192-223; Subnet Mask: /24; Networks: 2^21 = 2.1M; Hosts: 2^8 = 256.
  - **Class D**: 224-239 (Multicast).
  - **Class E**: 240-255 (Reserved).

## 3. IPv6 Addressing

- **Address Structure**: 128-bit (16 bytes); Total: 2^128 (340 trillion).
- **Shortening Rules**:
  - Leading zeros optional.
  - Consecutive zeros: Represent with `::` (only once).

## 4. Network vs. Broadcast Address

- **Network Address**: Start of a network (all host bits = 0).
- **Broadcast Address**: End of a network (all host bits = 1).
- **Hosts in a Network**: 2^(Host bits) - 2.
  - Example: `10.10.10.10/8`
    - Host Bits: 24; Network Address: `10.0.0.0`.
    - Broadcast Address: `10.255.255.255`.
    - Hosts: 2^24 - 2 = 16.7M.

## 5. Classful vs. Classless Addressing

- **Classful**: Subnet mask based on class (A=/8, B=/16, C=/24).
- **Classless**: Custom subnet mask (/27, /28, etc.).

## 6. Subnetting

- **Subnet Mask**: `/x` means x bits for network, (32-x) bits for host.
  - Example: `/18` = Network: 18 bits, Host: 14 bits; Subnet Mask: `255.255.192.0`.

### Subnetting via Hosts

- Example: `10.0.0.0/24` for 30 devices.
  - Add 2 to devices: 30 + 2 = 32.
  - Host Bits = log2(32) = 5; New Subnet Mask = `/27`.
  - New Network: `10.0.0.0/27`.
  - Broadcast: `10.0.0.31`.

### Subnetting via Networks

- Example: `10.10.10.0/24` into 4 subnets.
  - Networks: 2^2 = 4; Add 2 bits: `/26`.
  - Host Bits: 6 (2^6 = 64 per network).
  - Subnets:
    - NA0: `10.10.10.0/26`; BA0: `10.10.10.63`.
    - NA1: `10.10.10.64/26`; BA1: `10.10.10.127`.
    - NA2: `10.10.10.128/26`; BA2: `10.10.10.191`.
    - NA3: `10.10.10.192/26`; BA3: `10.10.10.255`.

## 7. Variable Length Subnet Mask (VLSM)

- Allows custom subnet sizes (e.g., 3, 5, 7 subnets).
- Example: `10.10.10.0/24` into 3 networks:
  - NA0: `10.10.10.0/25`; BA0: `10.10.10.127`.
  - NA1: `10.10.10.128/26`; BA1: `10.10.10.191`.
  - NA2: `10.10.10.192/26`; BA2: `10.10.10.255`.

## 8. Supernetting

- Combining smaller networks into larger ones.
- Example: Combine `192.168.10.0/24` to `192.168.13.0/24`:
  - Common Bits: `/21`.
  - Supernet: `192.168.8.0/21`.

## 9. IP Routing

- **Golden Rules**:
  1. Interfaces of the same router must be in different networks.
  2. Connections between routers must belong to the same network.

### Static Routing

- Add route:
  ```
  R1(config)# ip route <destination> <subnet> <gateway>
  ```
- View routing table:
  ```
  R1# show ip route
  ```

### Dynamic Routing (RIP)

- Enable RIP:
  ```
  R1(config)# router rip
  R1(config-router)# network <connected network>
  ```

## 10. VLAN Configuration

- **Create VLAN**:
  ```
  switch(config)# vlan 10
  switch(config-vlan)# name HPCSA
  ```
- **Access Mode (PC to Switch)**:
  ```
  switch(config-if)# switchport access vlan 10
  switch(config-if)# switchport mode access
  ```
- **Trunk Mode (Switch to Switch)**:
  ```
  switch(config-if)# switchport trunk encapsulation dot1q
  switch(config-if)# switchport mode trunk
  ```

## 11. Dynamic Host Configuration Protocol (DHCP)

- Configure DHCP:
  ```
  router(config)# ip dhcp pool HPCSA
  router(dhcp-config)# network <network> <subnet>
  router(dhcp-config)# default-router <gateway>
  ```

## 12. Command References

- **Switch Basic Commands**:
  - View running config: `switch# show running-config`.
  - Save config: `switch# write`.
- **Router Basic Commands**:
  - Assign IP: `router(config-if)# ip address <IP> <subnet>`.
  - Enable interface: `router(config-if)# no shutdown`.
  - View interfaces: `router# show ip interface brief`.

---

**Note**: Ensure you replace placeholders (e.g., `<destination>`, `<network>`) with actual values relevant to your setup.

