.filters {
    background-color: #FFFFFF;
    height: 70px;
    width: 100%;
    border: 1px solid #DDDDDD;
    border-radius: 4px;
    position: relative;
    display:flex;
}

.locations, .amenities {
    height: 100%;
    width: 25%;
    padding: 15px 40px;
    box-sizing: border-box;
}

.locations {
    border-right: 1px solid #DDDDDD;
}

.locations h3, .amenities h3 {
    font-weight: 600;
    margin: 0;
}

.locations h4, .amenities h4 {
    font-weight: 400;
    font-size: 14px;
    margin: 0;
}

.popover , .popover2{
    display: none;
    list-style-type: none;
    background-color: #FAFAFA;
    width: 25%;
    border: #DDDDDD solid 1px;
    border-radius: 4px; 
    position: absolute;
    top: 100%;
}

.popover li {
    list-style-type: none;
}

.locations:hover .popover {
    display: block;
}
.amenities:hover .popover2 {
    display: block;
}

.popover h2{
    font-size: 16px;
}

.button {
    font-size: 18px;
    background-color: #FF5A5F;
    color: #FFFFFF;
    height: 48px;
    width: 20%;
    border: none;
    border-radius: 4px;
    margin: 0;
    position: absolute;
    right: 30px;
    top: 50%;
    transform: translateY(-50%);
    opcaity: 1;
}

.button:hover {
    opacity: 0.9;
}
