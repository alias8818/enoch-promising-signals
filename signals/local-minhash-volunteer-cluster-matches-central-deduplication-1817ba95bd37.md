# Local minhash volunteer cluster matches central deduplication

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-minhash-volunteer-cluster-matches-central-deduplication-1817ba95bd37`
Run ID: `local-minhash-volunteer-cluster-matches-central-deduplication-1817ba95bd37-20260521T194634213666+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/230fe5f044c9

## What looked useful

The mechanism works in a bounded local simulation when LSH banding is tuned for the target similarity threshold. Default square-root LSH banding failed badly at low threshold, producing near-zero recall despite perfect precision.

## Boundaries and scale limits

Synthetic data only; no natural corpus, adversarial volunteer, privacy leakage, network churn, or million-document coordinator scaling was tested. Large signatures can exceed raw-text payload on short documents.

## Claim scope

On repeated synthetic clustered-text corpora of 600 documents split across 12 simulated volunteers, locally computed minhash signatures with one-row LSH bands recovered a central exact 5-shingle Jaccard dedup baseline at threshold 0.20 with mean pair F1 0.951 using 128 hashes and 56.2% of raw-text payload.

## Why it stopped

No-paper useful signal: synthetic evidence supports the mechanism but is insufficient for publication-grade validation.

## Recommended next action

Run the same harness on a public near-duplicate text benchmark with measured coordinator memory and network payload before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public-corpus volunteer minhash dedup validation
- Success threshold: At least one signature setting achieves pair F1 >= 0.95 against the central baseline with signature payload below 60% of raw text and no more than a 10x candidate-pair expansion over true central baseline pairs.
- Stop condition: Stop as negative if all signature settings either fall below 0.90 pair F1, exceed raw-text payload, or require candidate-pair expansion above 50x on the public corpus.

## Evidence references

- Artifact root: `<local-path>/projects/local-minhash-volunteer-cluster-matches-central-deduplication-1817ba95bd37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
