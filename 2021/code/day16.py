"""
As you leave the cave and reach open waters, you receive a transmission from the Elves back on the ship.

The transmission was sent using the Buoyancy Interchange Transmission System (BITS), a method of packing numeric expressions into a binary sequence. Your submarine's computer has saved the transmission in hexadecimal (your puzzle input).

The first step of decoding the message is to convert the hexadecimal representation into binary. Each character of hexadecimal corresponds to four bits of binary data:

0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111
The BITS transmission contains a single packet at its outermost layer which itself contains many other packets. The hexadecimal representation of this packet might encode a few extra 0 bits at the end; these are not part of the transmission and should be ignored.

Every packet begins with a standard header: the first three bits encode the packet version, and the next three bits encode the packet type ID. These two values are numbers; all numbers encoded in any packet are represented as binary with the most significant bit first. For example, a version encoded as the binary sequence 100 represents the number 4.

Packets with type ID 4 represent a literal value. Literal value packets encode a single binary number. To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits, and then it is broken into groups of four bits. Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit. These groups of five bits immediately follow the packet header. For example, the hexadecimal string D2FE28 becomes:

110100101111111000101000
VVVTTTAAAAABBBBBCCCCC
Below each bit is a label indicating its purpose:

The three bits labeled V (110) are the packet version, 6.
The three bits labeled T (100) are the packet type ID, 4, which means the packet is a literal value.
The five bits labeled A (10111) start with a 1 (not the last group, keep reading) and contain the first four bits of the number, 0111.
The five bits labeled B (11110) start with a 1 (not the last group, keep reading) and contain four more bits of the number, 1110.
The five bits labeled C (00101) start with a 0 (last group, end of packet) and contain the last four bits of the number, 0101.
The three unlabeled 0 bits at the end are extra due to the hexadecimal representation and should be ignored.
So, this packet represents a literal value with binary representation 011111100101, which is 2021 in decimal.

Every other type of packet (any packet with a type ID other than 4) represent an operator that performs some calculation on one or more sub-packets contained within. Right now, the specific operations aren't important; focus on parsing the hierarchy of sub-packets.

An operator packet contains one or more packets. To indicate which subsequent binary data represents its sub-packets, an operator packet can use one of two modes indicated by the bit immediately after the packet header; this is called the length type ID:

If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.

For example, here is an operator packet (hexadecimal string 38006F45291200) with length type ID 0 that contains two sub-packets:

00111000000000000110111101000101001010010001001000000000
VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB
The three bits labeled V (001) are the packet version, 1.
The three bits labeled T (110) are the packet type ID, 6, which means the packet is an operator.
The bit labeled I (0) is the length type ID, which indicates that the length is a 15-bit number representing the number of bits in the sub-packets.
The 15 bits labeled L (000000000011011) contain the length of the sub-packets in bits, 27.
The 11 bits labeled A contain the first sub-packet, a literal value representing the number 10.
The 16 bits labeled B contain the second sub-packet, a literal value representing the number 20.
After reading 11 and 16 bits of sub-packet data, the total length indicated in L (27) is reached, and so parsing of this packet stops.

As another example, here is an operator packet (hexadecimal string EE00D40C823060) with length type ID 1 that contains three sub-packets:

11101110000000001101010000001100100000100011000001100000
VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC
The three bits labeled V (111) are the packet version, 7.
The three bits labeled T (011) are the packet type ID, 3, which means the packet is an operator.
The bit labeled I (1) is the length type ID, which indicates that the length is a 11-bit number representing the number of sub-packets.
The 11 bits labeled L (00000000011) contain the number of sub-packets, 3.
The 11 bits labeled A contain the first sub-packet, a literal value representing the number 1.
The 11 bits labeled B contain the second sub-packet, a literal value representing the number 2.
The 11 bits labeled C contain the third sub-packet, a literal value representing the number 3.
After reading 3 complete sub-packets, the number of sub-packets indicated in L (3) is reached, and so parsing of this packet stops.

For now, parse the hierarchy of the packets throughout the transmission and add up all of the version numbers.

Here are a few more examples of hexadecimal-encoded transmissions:

8A004A801A8002F478 represents an operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6); this packet has a version sum of 16.
620080001611562C8802118E34 represents an operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values. This packet has a version sum of 12.
C0015000016115A2E0802F182340 has the same structure as the previous example, but the outermost packet uses a different length type ID. This packet has a version sum of 23.
A0016C880162017C3686B18A3D4780 is an operator packet that contains an operator packet that contains an operator packet that contains five literal values; it has a version sum of 31.
"""

import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s %(message)s")


def read_vals() -> list:
    with open("../data/day16data.txt", "r") as file:
        lines = file.read().splitlines()

        return lines[0]


def recur(init):

    version = int(init[:3], 2)
    type_id = int(init[3:6], 2)
    packet = init[6:]

    log.info(f"version = {version}, type_id = {type_id}")
    if type_id == 4:  # literal packet
        while packet[0] == "1":
            packet = packet[5:]
        packet = packet[
            5:
        ]  # for this type, we only have 1 type_id so just skip them till the end 5 bits and return
        return packet, version

    length_id = packet[0]
    packet = packet[1:]

    if length_id == "0":
        total_length = int(packet[:15], 2)
        subpacket = packet[15 : 15 + total_length]
        packet = packet[15 + total_length :]
        # For each subpacket inside the current packet, update the total version count
        while len(subpacket) != 0:
            subpacket, subversion = recur(subpacket)
            version += subversion
    else:
        num_packets = int(packet[:11], 2)
        packet = packet[11:]
        # For each subpacket inside the current packet, update the total version count
        for i in range(num_packets):
            packet, subversion = recur(packet)
            version += subversion
    return packet, version


def recur_2(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    packet = packet[6:]
    subvalues = []

    if type_id == 4:
        value = ""
        while packet[0] == "1":
            value += packet[1:5]
            packet = packet[5:]
        value += packet[1:5]
        packet = packet[5:]
        # Return the remaining subpackets and the value of the current one
        return packet, int(value, 2)

    length_id = packet[0]
    packet = packet[1:]
    if length_id == "0":
        total_length = int(packet[:15], 2)
        subpacket = packet[15 : 15 + total_length]
        packet = packet[15 + total_length :]

        while len(subpacket) != 0:
            # Add the values for each subpacket to the overall values
            subpacket, subvalue = recur_2(subpacket)
            subvalues.append(subvalue)
    else:
        num_packets = int(packet[:11], 2)
        packet = packet[11:]

        for i in range(num_packets):
            packet, subvalue = recur_2(packet)
            subvalues.append(subvalue)

    if type_id == 0:
        value = sum(subvalues)
    elif type_id == 1:
        value = 1
        for k in subvalues:
            value *= k
    elif type_id == 2:
        value = min(subvalues)
    elif type_id == 3:
        value = max(subvalues)
    elif type_id == 5:
        value = int(subvalues[0] > subvalues[1])
    elif type_id == 6:
        value = int(subvalues[0] < subvalues[1])
    elif type_id == 7:
        value = int(subvalues[0] == subvalues[1])

    return packet, value


def part2(init):
    value = recur_2(init)[1]
    return value


def part1(init):

    version = recur(init)[1]

    return version


if __name__ == "__main__":
    log.info("Load data into memory...")
    data = read_vals()
    init = ""
    log.info("Convert data into binary format...")
    for i in data:
        init += bin(int(i, 16))[2:].zfill(4)

    log.info(f"Part 1: {part1(init)}")
    log.info(f"Part 2: {part2(init)}")
