CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM telefony WHERE name = p_name) THEN
        UPDATE telefony SET phone = p_phone WHERE name = p_name;
    ELSE 
        INSERT INTO telefony(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;


 
CREATE OR REPLACE PROCEDURE delete_contact_flexible(p_ident VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM telefony WHERE name = p_ident OR phone = p_ident;
END;
$$;


CREATE OR REPLACE PROCEDURE bulk_insert_contacts(names VARCHAR[], phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    
    FOR i IN 1 .. array_length(names, 1) LOOP
        
        IF length(phones[i]) >= 10 THEN
            INSERT INTO phonebook(name, phone) 
            VALUES(names[i], phones[i])
            ON CONFLICT (name) DO UPDATE SET phone = phones[i];
        END IF;
    END LOOP;
END;
$$;