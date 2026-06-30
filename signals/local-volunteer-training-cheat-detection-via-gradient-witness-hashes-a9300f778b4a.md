# Local volunteer-training cheat detection via gradient witness hashes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-volunteer-training-cheat-detection-via-gradient-witness-hashes-a9300f778b4a`
Run ID: `local-volunteer-training-cheat-detection-via-gradient-witness-hashes-a9300f778b4a-20260528T214343337361+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0390c3e9c4a0

## What looked useful

128-bit SimHash witnesses over 1,000 seeds rejected naive/wrong/stale gradient scenarios, but both adaptive valid-hash/zero-update and valid-hash/wrong-update attacks passed hash-only verification at 100%. Increasing hash length from 32 to 256 bits did not change this adaptive failure.

## Boundaries and scale limits

Toy logistic regression only; synthetic IID/non-IID shifts only; no real neural-network training, privacy-preserving data setting, secure challenge protocol, or multi-round adversarial deployment. The verifier was given the favorable ability to recompute the expected witness.

## Claim scope

In a synthetic logistic-regression volunteer-training proxy where the verifier can recompute assigned-gradient SimHash witnesses, gradient witness hashes reject naive random, wrong-client, label-flipped, and stale gradients, but hash-only verification does not prove that the submitted update corresponds to the witnessed gradient.

## Why it stopped

Proxy evidence shows a protocol-level insufficiency in hash-only gradient witnesses rather than a full validation failure at model scale.

## Recommended next action

Stop this run as a no-paper useful signal; next concrete work is a bounded update-bound witness protocol test that must accept honest multi-step local training while rejecting valid-hash wrong-update attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Update-bound gradient witness protocol for multi-step volunteer training
- Success threshold: At least 0.99 honest multi-step acceptance and at least 0.99 rejection of valid-hash zero-update and valid-hash wrong-update attacks over 500 or more seeded trials, with witness overhead below 10% of local training time.
- Stop condition: Stop if the binding rule either rejects more than 5% of honest multi-step runs, leaves either adaptive attack above 5% pass rate, or costs roughly as much as recomputing the full training trajectory.

## Evidence references

- Artifact root: `<local-path>/projects/local-volunteer-training-cheat-detection-via-gradient-witness-hashes-a9300f778b4a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
