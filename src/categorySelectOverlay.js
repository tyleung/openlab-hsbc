import React, { Component } from 'react';

class CategorySelectOverlay extends Component {
  render() {
    return (
      <div className="category-select-overlay form-group">
        <select
          className="form-control"
          onChange={this.props.onChange}
          id="sel1"
        >
          <option>Food</option>
          <option>Beauty</option>
          <option>Books</option>
          <option>Electronics</option>
          <option>Toys</option>
        </select>
      </div>
    );
  }
}

export default CategorySelectOverlay;
