# install flask from pip3
package { 'werkzeug':
    ensure   => '2.0.2',
    provider => 'pip',
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip',
}