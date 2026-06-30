# Evidence Ledger for Volunteer/Home Distributed Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-volunteer-home-distributed-training-88f5aa11beb4`
Run ID: `evidence-ledger-for-volunteer-home-distributed-training-88f5aa11beb4-20260613T132427477411+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0fcb32ee4097

## What looked useful

The prototype detected 5/5 injected tampering/replay/fork attack classes that an unsigned manifest detected 0/5 times, with 53 MB max RSS and 3.57 seconds wall-clock for the bounded measurement.

## Boundaries and scale limits

Test used synthetic updates, keyed digests instead of public-key signatures, one local process, no real networking, no heterogeneous home nodes, no actual model convergence measurement, and no production adversary model.

## Claim scope

A local synthetic evidence ledger for volunteer/home distributed training can detect the five tested contribution-integrity failures while verifying 6,400 contribution records at about 133k records/second with 1.39x storage overhead versus an unsigned manifest.

## Why it stopped

Closed as no-paper useful signal because this run validated only a local synthetic ledger mechanism, not a real volunteer/home distributed training deployment.

## Recommended next action

Run a bounded direct follow-up on a real small distributed training job with public-key worker identities, network partitions/rejoins, malicious workers, and convergence/throughput comparison against a no-ledger control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger on Real Small Distributed Training
- Success threshold: Detect all injected integrity attacks with no false acceptance and keep median training throughput degradation below 5% relative to the no-ledger control.
- Stop condition: Stop if any injected integrity attack is accepted as valid, or if ledger overhead exceeds 15% in two repeated controlled runs.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-volunteer-home-distributed-training-88f5aa11beb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
