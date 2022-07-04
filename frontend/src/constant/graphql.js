import gql from "graphql-tag";

export const BOOK_LIST_QUERY = gql`
    query Books {
        books {
            id
            title
            author
            isbn
            pages
            price
            quantity
            description
            status
            dateCreated
        }
    }
`;
