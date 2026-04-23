CREATE OR REPLACE FUNCTION get_contacts_pattern(p_search TEXT)
RETURNS TABLE(contact_id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.contact_id, c.name, c.phone
    FROM telefony c
    WHERE c.name ILIKE '%' || p_search || '%'
       OR c.phone ILIKE '%' || p_search || '%'
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_peginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.contact_id, c.name, c.phone FROM telefony c
    ORDER BY c.contact_id LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;


