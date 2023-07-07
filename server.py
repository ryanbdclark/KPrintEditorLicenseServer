import pydivert
import re
import pyuac

def main():
    with pydivert.WinDivert("udp.SrcPort == 1791") as w:
        for packet in w:
            payload = packet.payload
            payload = re.sub(
                b"[\d][\+][\d]{1,3}[\+][\d]{1,3}[\+][\d]{1,3}[\+][\d]{1,3}[\+][A-z0-9]*[\+]ql1117[\+]",
                b"0+2147483647+1+1+1+hacked+hostnamegoeshere+",
                payload,
            )
            packet.payload = payload

            w.send(packet)

            print(f"Packet intercepted from {packet.src_addr}, license values amended: Printers: 2147483647, Editor: True, Fax: True, SMS: True")


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main()
