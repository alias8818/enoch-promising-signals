# MinHash fuzzy dedup at tiny scale: does 0.8 threshold beat no-dedup?

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-fuzzy-dedup-at-tiny-scale-does-0-8-threshold-beat-no-dedup-9490c3ef471b`
Run ID: `minhash-fuzzy-dedup-at-tiny-scale-does-0-8-threshold-beat-no-dedup-9490c3ef471b-20260621T234842252997+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ef97128d263b

## What looked useful

Threshold 0.8 produced zero false drops and zero cluster loss in the sweep, but duplicate-drop recall fell from 0.57-0.65 for very close copies to about 0.16 at mutation_rate 0.05 and near zero at mutation_rate >=0.10, leaving almost all fuzzy duplicates retained.

## Boundaries and scale limits

Synthetic text only; 40 trials per setting; no real corpus labels; no downstream model or retrieval evaluation; single streaming order; n_base=30 with duplicate factors 1 and 3.

## Claim scope

In controlled tiny synthetic corpora of 72-132 documents with known duplicate clusters, 128-permutation MinHash over 5-token shingles at threshold 0.8 acts as a high-precision near-exact duplicate filter but not as a broad fuzzy dedup improvement over no-dedup.

## Why it stopped

Proxy/synthetic evidence is sufficient to reject the broad tiny-scale claim that 0.8 fuzzy MinHash generally beats no-dedup, but it is not full validation on real corpora.

## Recommended next action

Stop this run as a bounded synthetic early falsification; the next useful action is a small labeled real-corpus threshold sweep against no-dedup with downstream retrieval or training metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus MinHash threshold sweep at tiny scale
- Success threshold: Find a threshold/policy that removes at least 50% of labeled harmful near-duplicates, keeps unique-cluster loss below 1%, and improves the downstream proxy versus no-dedup by a predeclared margin.
- Stop condition: Stop if no threshold removes at least 25% of harmful near-duplicates at below 1% unique-cluster loss, or if downstream proxy metrics do not improve over no-dedup.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-fuzzy-dedup-at-tiny-scale-does-0-8-threshold-beat-no-dedup-9490c3ef471b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
