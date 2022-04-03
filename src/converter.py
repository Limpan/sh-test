import click
import xml.etree.ElementTree as ET


class ParseError(Exception):
    pass


def convert_to_xml(data):
    root = ET.Element('people')

    stack = [root]

    for line in data:
        tag, *values = line.split('|')



        if tag == "P":
            if stack[-1].tag == "family":
                stack.pop()
            if stack[-1].tag == "person":
                stack.pop()

            person = ET.SubElement(stack[-1], "person")
            firstname = ET.SubElement(person, "firstname")
            firstname.text = values[0]
            lastname = ET.SubElement(person, "lastname")
            lastname.text = values[1]

            stack.append(person)

        elif tag == "T" and stack[-1].tag in ["person", "family"]:
            phone = ET.SubElement(stack[-1], "phone")
            mobile = ET.SubElement(phone, "mobile")
            mobile.text = values[0]
            landline = ET.SubElement(phone, "landline")
            landline.text = values[1]


        elif tag == "A" and stack[-1].tag in ["person", "family"]:
            address = ET.SubElement(stack[-1], "address")
            street = ET.SubElement(address, "street")
            street.text = values[0]
            city = ET.SubElement(address, "city")
            city.text = values[1]
            postcode = ET.SubElement(address, "postcode")
            postcode.text = values[2]

        elif tag == "F" and stack[-1].tag in ["person", "family"]:
            if stack[-1].tag == "family":
                stack.pop()

            family = ET.SubElement(stack[-1], "family")
            name = ET.SubElement(family, "name")
            name.text = values[0]
            born = ET.SubElement(family, "born")
            born.text = values[1]

            stack.append(family)

        else:
            raise ParseError("\n{}\n{}".format(line, stack[-1].tag))


    return root


@click.command()
def main():
    click.echo("Hello")


if __name__ == "__main__":
    main()
