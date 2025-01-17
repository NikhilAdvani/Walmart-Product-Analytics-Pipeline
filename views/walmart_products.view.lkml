view: walmart_products {
  sql_table_name: `your-project.walmart_analytics.product_data` ;;

  dimension: id {
    primary_key: yes
    type: number
    sql: ${TABLE}.id ;;
  }

  dimension: title {
    type: string
    sql: ${TABLE}.title ;;
  }

  dimension: price {
    type: number
    sql: ${TABLE}.price ;;
    value_format_name: usd
  }

  dimension: category {
    type: string
    sql: ${TABLE}.category ;;
  }

  dimension: rating_rate {
    type: number
    sql: ${TABLE}.rating.rate ;;
    value_format_name: decimal_2
  }

  dimension: rating_count {
    type: number
    sql: ${TABLE}.rating.count ;;
  }

  dimension: price_tier {
    type: string
    sql: ${TABLE}.price_tier ;;
  }

  measure: average_price {
    type: average
    sql: ${price} ;;
    value_format_name: usd
  }

  measure: average_rating {
    type: average
    sql: ${rating_rate} ;;
    value_format_name: decimal_2
  }

  measure: total_products {
    type: count
    drill_fields: [id, title, price, category, rating_rate]
  }
} 