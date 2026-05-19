# Commit-Reveal Shard Lottery for Volunteer Gradient Validation

Status: `useful_signal`
Project ID: `commit-reveal-shard-lottery-for-volunteer-gradient-validation-385eda026ea7`
Run ID: `commit-reveal-shard-lottery-for-volunteer-gradient-validation-385eda026ea7-20260518T214959692492+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9941cbfc3334

## What looked useful

Commit-reveal removes the trivial adaptive evasion of preannounced shard audits and matches the expected detection/cost frontier, but sparse corruptions remain expensive to detect; at 128 shards and 16 audited shards, single-shard corruption detection was only about 0.11 at 12.5% audit coverage.

## Boundaries and scale limits

No full ML training loop, real Merkle proof verification, real volunteer network, incentive model, Sybil/collusion defense, or high-sensitivity coordinate attack was tested. Shard counts were limited to 32, 64, and 128.

## Claim scope

Protocol-level simulation of commit-before-sample shard auditing for volunteer gradient validation across 576 configurations with 5,000 Monte Carlo trials each, checked against analytic detection probabilities.

## Why it stopped

Proxy protocol evidence supports the commit-reveal mechanism but does not validate end-to-end volunteer gradient training; sparse corruption detection is too coverage-limited for a paper claim from this run alone.

## Recommended next action

Run one bounded deepen follow-up that embeds the lottery in a toy SGD/federated-learning loop and measures model-quality degradation under random and targeted shard attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end SGD shard-lottery validation under targeted corruptions
- Success threshold: At <=25% validation cost, the lottery arm detects or neutralizes broad corruptions with final validation loss within 5% of full validation and materially better than no validation; targeted sparse attacks must either be detected at >=0.8 probability or shown to have limited model impact.
- Stop condition: Stop as negative if targeted sparse corruptions cause >10% worse final validation loss than full validation at <=25% audit cost or if detection remains below 0.5 for high-impact sparse attacks.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-shard-lottery-for-volunteer-gradient-validation-385eda026ea7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
