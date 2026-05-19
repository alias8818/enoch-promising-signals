# Held-out adversarial paraphrase benchmark for hybrid signed-shard poison scanning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-adversarial-paraphrase-benchmark-for-hybrid-signe-9f09a96b0c`
Run ID: `held-out-adversarial-paraphrase-benchmark-for-hybrid-signe-9f09a96b0c-20260519T063346364162+0000`

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

- Internal Enoch project: Held-out adversarial paraphrase benchmark for hybrid signed-shard poison scanning: internal_generated:held-out-adversarial-paraphrase-benchmark-for-hybrid-signe-9f09a96b0c

## What looked useful

Exact signatures were precise but brittle (0.2857 mean recall). TF-IDF semantic matching and the hybrid reached about 0.54 mean recall at 1.00 measured precision, but hybrid recall matched semantic-only recall and was 0.0 on semantic_gap and obfuscated held-out attacks.

## Boundaries and scale limits

Synthetic poison shards and generated paraphrases only; no public poisoned corpus, production retrieval traces, neural embedding models, LLM paraphrase adversary, or end-to-end downstream model harm reduction were tested.

## Claim scope

On a deterministic synthetic benchmark with 96 signed poison shards per seed and five fixed seeds, lexical semantic nearest-neighbor scanning improves recall over normalized exact signatures, but the tested exact-plus-semantic hybrid does not improve over semantic-only TF-IDF and fails several held-out adversarial paraphrase styles.

## Why it stopped

Tier 2 evidence is mixed: mechanism improves over exact signatures but does not beat the real semantic baseline and misses key held-out adversarial paraphrases.

## Recommended next action

Stop this run as no-paper evidence; a bounded deepen follow-up should replace lexical TF-IDF with a stronger semantic detector and require a clear lift over semantic-only matching on the same held-out attack families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural semantic detector ablation for signed-shard paraphrase poison scanning
- Success threshold: Mean held-out recall >= 0.80 at validation precision >= 0.95, with hybrid F1 at least 0.05 above semantic-only and nonzero recall on every held-out attack family.
- Stop condition: Stop if the neural hybrid still matches semantic-only performance or if semantic_gap/obfuscated recall remains below 0.25 at the precision constraint.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-adversarial-paraphrase-benchmark-for-hybrid-signe-9f09a96b0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
