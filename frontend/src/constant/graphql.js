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

export const CATEGORY_LIST_QUERY = gql`
  query Categories {
    categories {
      id
      title
    }
  }
`;

export const GROCERY_LIST_QUERY = gql`
  query Groceries {
    groceries {
      productTag
      name
      category {
        id
        title
      }
      price
      quantity
      imageurl
      status
      dateCreated
    }
  }
`;
