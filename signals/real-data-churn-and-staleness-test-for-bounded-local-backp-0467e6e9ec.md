# Real-data churn and staleness test for bounded local backprop

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-data-churn-and-staleness-test-for-bounded-local-backp-0467e6e9ec`
Run ID: `real-data-churn-and-staleness-test-for-bounded-local-backp-0467e6e9ec-20260607T063618527181+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Volunteer Distributed Training with Bounded Local Backprop: enoch://control-plane/projects/volunteer-distributed-training-with-bounded-local-backprop-a9ff9066e0fd/runs/volunteer-distributed-training-with-bounded-local-backprop-a9ff9066e0fd-20260605T211228723884+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1fd369b1bf6e

## What looked useful

Delay-4 stale boundary gradients lost 7.47 percentage points of mean test accuracy versus fresh delay 0, exceeding the 2.0 percentage point tolerance threshold; feature drift rose with delay and delay 16 degraded sharply.

## Boundaries and scale limits

Does not cover transformers, language modeling, larger parameter scales, convolutional architectures, multi-node asynchronous training, learned synthetic gradients, or staleness mitigation methods.

## Claim scope

Small direct real-data test of stale boundary-gradient bounded local backprop on a 784-256-128-10 MLP trained on 20,000 Fashion-MNIST examples and evaluated on 5,000 test examples across three seeds.

## Why it stopped

Controlled small direct Fashion-MNIST stale-boundary-gradient test falsified the delay-4 tolerance threshold; this is an early direct negative result rather than full-scale validation.

## Recommended next action

Stop this no-paper run; a bounded follow-up should test an explicit stale-gradient mitigation on the same setup before any larger-scale training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stale-gradient mitigation test for bounded local backprop
- Success threshold: Mitigated delay 4 loses no more than 2.0 percentage points of mean test accuracy versus fresh delay 0 and improves by at least 4.0 percentage points over unmitigated delay 4.
- Stop condition: Stop if mitigated delay 4 still loses more than 2.0 percentage points versus fresh delay 0 or if the improvement is explained solely by reducing the upstream learning rate.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-churn-and-staleness-test-for-bounded-local-backp-0467e6e9ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
