"""Independent packaging/mass arithmetic checks; not engineering validation.

Run from any directory. --svg-dir additionally checks regenerated SVG structure
and clipping of text anchors. Uses only the Python standard library.
"""
import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def check(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--svg-dir', type=Path)
    args = parser.parse_args()
    g = json.loads((Path(__file__).resolve().parent / 'geometry.json').read_text())
    b, l, p, bar = g['brick'], g['laptop'], g['backpack'], g['bar']
    full, half = b['finished_max_full_mm'], b['finished_max_half_mm']
    edge, gap = g['grid']['edge_clearance_mm'], g['grid']['intermodule_gap_mm']
    check(l['cassette_inner_mm'][0] == 4*full[0]+3*gap+2*edge, 'Laptop finished grid length')
    check(l['cassette_inner_mm'][1] == full[1]+2*edge, 'Laptop finished grid depth')
    check(p['carrier_inner_mm'][0] == 3*full[0]+2*gap+2*edge, 'Big Pack finished grid width')
    check(p['carrier_inner_mm'][1] == 3*full[1]+2*gap+2*edge, 'Big Pack finished grid height')
    for q, inner, outer, index in [(l,'cassette_inner_mm','cassette_outer_mm',2),(p,'carrier_inner_mm','carrier_outer_mm',2)]:
        check(all(o-i == 8 for o,i in zip(q[outer],q[inner])), '4mm enclosure face allowances')
        check(q['stack_max_mm']+q['clamp_mm']+q['clamp_reserve_mm'] == q[inner][index], 'Stack leaves clamp and reserve')
        check(all(bay > out for bay,out in zip(q['bay_mm'],q[outer])), 'Bay must exceed enclosure')
    check(2*full[2]+half[2] == l['stack_max_mm'], 'Full/full/half stack')
    check(full[2]+half[2] == p['stack_max_mm'], 'Big Pack full/half stack')
    check(all(hatch > tray for hatch,tray in zip(l['hatch_clear_mm'], l['cassette_outer_mm'][1:])), 'Clear hatch fit')
    check(l['base_under_cassette_mm']+l['cassette_outer_mm'][2] == l['cassette_top_mm'], 'Cassette elevation')
    check(l['bay_top_mm']+l['barrier_mm']+l['impact_pad_mm']+l['free_gap_mm'] == l['sleeve_bottom_mm'], 'Laptop isolation stack')
    check(l['sleeve_bottom_mm']+l['sleeve_outer_mm'][1]+l['top_allowance_mm'] == l['body_mm'][1], 'Laptop body height stack')
    for bottom in (p['low_carrier_bottom_mm'],p['midlow_carrier_bottom_mm']):
        check(bottom-6 >= 0 and bottom+p['carrier_outer_mm'][1]+6 <= p['body_mm'][1], 'Alternative bay fit')
    check(p['midlow_carrier_bottom_mm']-p['low_carrier_bottom_mm'] == 30, 'Placement trial offset')
    check(p['rear_pad_frame_mm']+p['bay_mm'][2]+p['barrier_mm']+p['lateral_isolation_mm']+p['sleeve_outer_mm'][2]+41 == p['body_mm'][2], 'Backpack depth stack')
    check(14+p['impact_pad_mm']+p['vertical_free_gap_mm'] == p['sleeve_bottom_mm'], 'Backpack vertical isolation')
    check(p['sleeve_bottom_mm']+p['sleeve_outer_mm'][1] <= p['body_mm'][1], 'Portrait sleeve height')
    for q in (l,p):
        check(q['sleeve_outer_mm'][0] < q['body_mm'][0], 'Padded sleeve width')
    allowance = g['total_mass_limit_kg']-g['example_empty_bag_kg']-g['example_laptop_kg']-g['example_other_contents_kg']
    f,h=b['nominal_full_kg'],b['nominal_half_kg']
    check(allowance == 24 and 4*(2*f+h) == 25 > allowance, 'Reject false 24kg full loading')
    check(8*f+3*h == 9*f+h == 23.75 <= allowance, 'Candidate nominal loading arithmetic')
    core_mass = b['steel_density_kg_m3']
    for d in b['core_nominal_mm']: core_mass *= d/1000
    check(2.460 < core_mass < 2.462 and core_mass != f, 'Dimensions do not guarantee nominal mass')
    for name,q in [('laptop',l),('backpack',p)]:
        finished=bar[f'{name}_finished_max_mm'];raw=bar[f'{name}_raw_mm']
        check(all(x > y for x,y in zip(finished,raw)), 'Sleeve coating allowance')
        length,depth=(q['cassette_inner_mm'][:2] if name=='laptop' else q['carrier_inner_mm'][:2])
        check(finished[0] <= length and finished[1] <= depth, 'Sleeved bar cavity fit')
    check(7*bar['laptop_finished_max_mm'][2] <= l['stack_max_mm'] < 8*bar['laptop_finished_max_mm'][2], 'Seven bars fit, eight do not')
    check(2*104+gap+2*edge <= p['carrier_inner_mm'][1] < 3*104+2*gap+2*edge, 'Only two sleeved bar rows fit with clearance')
    check(4*12 <= p['stack_max_mm'], 'Four backpack bar layers fit')
    if args.svg_dir:
        ns={'s':'http://www.w3.org/2000/svg'}
        for name in ('1-laptop-bag','2-big-pack','3-weight-system'):
            root=ET.parse(args.svg_dir/f'{name}.svg').getroot()
            check(root.attrib['viewBox']=='0 0 1680 1188', 'Expected sheet size')
            texts=root.findall('.//s:text',ns)
            check(any('NOT ENGINEERING VALIDATED' in ''.join(t.itertext()) for t in texts), 'Missing provisional warning')
            for t in texts:
                x,y=float(t.attrib['x']),float(t.attrib['y'])
                check(20 <= x <= 1660 and 20 <= y <= 1168, f'{name}: text anchor off page at{x},{y}')
    print('PASS: finished envelopes, insertion, clamp/isolation stacks and mass counterexamples')
    print('NOT a strength, ergonomics or impact-safety validation')


if __name__ == '__main__':
    main()
