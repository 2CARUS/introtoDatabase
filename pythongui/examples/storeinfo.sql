SELECT store.store_name, store.store_phone, store.store_email, address.building_number, address.street, address.apartment, address.city, address.state,address.country,address.zip FROM store
    join address on store.store_address_id = address.address_id
    where store.store_name = 'Toolhouse on 35W'