from converter import convert_to_xml

def test_no_data_return_empty():
    data = []

    rv = convert_to_xml(data)

    assert rv.tag == "people"


def test_single_person_no_info():
    data = ["P|Victoria|Bernadotte"]

    rv = convert_to_xml(data)

    assert rv.find("./person/firstname").text == "Victoria"
    assert rv.find("./person/lastname").text == "Bernadotte"


def test_single_person_with_phone():
    data = ["P|Victoria|Bernadotte", 
            "T|070-0101010|0459-123456"]

    rv = convert_to_xml(data)

    assert rv.find("./person/phone/mobile").text == "070-0101010"
    assert rv.find("./person/phone/landline").text == "0459-123456"


def test_single_person_with_addrees():
    data = ["P|Victoria|Bernadotte", 
            "A|Haga Slott|Stockholm|10100"]

    rv = convert_to_xml(data)

    assert rv.find("./person/address/street").text == "Haga Slott"
    assert rv.find("./person/address/city").text == "Stockholm"
    assert rv.find("./person/address/postcode").text == "10100"


def test_single_person_with_family():
    data = ["P|Victoria|Bernadotte", 
            "F|Estelle|2012"]

    rv = convert_to_xml(data)

    assert rv.find("./person/family/name").text == "Estelle"
    assert rv.find("./person/family/born").text == "2012"


def test_single_person_with_all_info():
    data = ["P|Victoria|Bernadotte", 
            "T|070-0101010|0459-123456", 
            "A|Haga Slott|Stockholm|10100", 
            "F|Estelle|2012"]

    rv = convert_to_xml(data)

    assert rv.find("./person/phone/mobile").text == "070-0101010"
    assert rv.find("./person/phone/landline").text == "0459-123456"
    assert rv.find("./person/address/street").text == "Haga Slott"
    assert rv.find("./person/address/city").text == "Stockholm"
    assert rv.find("./person/address/postcode").text == "10100"
    assert rv.find("./person/family/name").text == "Estelle"
    assert rv.find("./person/family/born").text == "2012"


def test_multiple_persons_no_info():
    data = ["P|Victoria|Bernadotte",
            "P|Joe|Biden"]
    
    rv = convert_to_xml(data)

    assert len(rv.findall("./person")) == 2
    assert rv.findall("./person")[0].find("firstname").text == "Victoria"
    assert rv.findall("./person")[0].find("lastname").text == "Bernadotte"
    assert rv.findall("./person")[1].find("firstname").text == "Joe"
    assert rv.findall("./person")[1].find("lastname").text == "Biden"


def test_multiple_persons_with_lots_of_data():
    data = ["P|Victoria|Bernadotte",
            "T|070-0101010|0459-123456",
            "A|Haga Slott|Stockholm|10100",
            "F|Estelle|2012",
            "A|Solliden|Öland|10002",
            "F|Oscar|2016",
            "T|0702-020202|02-202020",
            "P|Joe|Biden",
            "A|White House|Washington, D.C|20500"]
    
    rv = convert_to_xml(data)

    import xml.etree.ElementTree as ET

    ET.dump(rv)

    assert len(rv.findall("./person")) == 2

    # Check first person
    assert rv.findall("./person")[0].find("firstname").text == "Victoria"
    assert rv.findall("./person")[0].find("lastname").text == "Bernadotte"
    assert rv.findall("./person")[0].find("phone/mobile").text == "070-0101010"
    assert rv.findall("./person")[0].find("phone/landline").text == "0459-123456"
    assert rv.findall("./person")[0].find("address/street").text == "Haga Slott"
    assert rv.findall("./person")[0].find("address/city").text == "Stockholm"
    assert rv.findall("./person")[0].find("address/postcode").text == "10100"

    # Check family of first person
    assert rv.findall("./person")[0].findall("family")[0].find("name").text == "Estelle"
    assert rv.findall("./person")[0].findall("family")[0].find("born").text == "2012"
    assert rv.findall("./person")[0].findall("family")[0].find("address/street").text == "Solliden"
    assert rv.findall("./person")[0].findall("family")[0].find("address/city").text == "Öland"
    assert rv.findall("./person")[0].findall("family")[0].find("address/postcode").text == "10002"

    assert rv.findall("./person")[0].findall("family")[1].find("name").text == "Oscar"
    assert rv.findall("./person")[0].findall("family")[1].find("born").text == "2016"
    assert rv.findall("./person")[0].findall("family")[1].find("phone/mobile").text == "0702-020202"
    assert rv.findall("./person")[0].findall("family")[1].find("phone/landline").text == "02-202020"

    # Check second person
    assert rv.findall("./person")[1].find("firstname").text == "Joe"
    assert rv.findall("./person")[1].find("lastname").text == "Biden"
    assert rv.findall("./person")[1].find("address/street").text == "White House"
    assert rv.findall("./person")[1].find("address/city").text == "Washington, D.C"
    assert rv.findall("./person")[1].find("address/postcode").text == "20500"
