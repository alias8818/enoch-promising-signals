# Small-LM Direct KV Intervention for Exact Anchors plus Log-Count Summaries

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-lm-direct-kv-intervention-for-exact-anchors-plus-log-98b1dc3c48`
Run ID: `small-lm-direct-kv-intervention-for-exact-anchors-plus-log-98b1dc3c48-20260518T194504151122+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/13ecdec67f00

## What looked useful

Across three seeds, correct injected KV reached 100% exact value accuracy and 100% log-count accuracy, while no-KV averaged 0.0082 value / 0.0765 count accuracy and shuffled controls stayed around 0.08 mixed-task accuracy. Attention diagnostics showed high mass on the queried anchor only when keys matched.

## Boundaries and scale limits

Synthetic tables only; purpose-built trainable direct-KV module only; no pretrained GPT-2-small-class native past_key_values intervention; no natural-language corpus, long-context serving, robustness, or publication-grade baseline suite.

## Claim scope

In a controlled synthetic task, a 556,941-parameter transformer with externally injected key/value memory slots can answer exact anchor lookup and log-count bucket queries from fresh per-example tables, while no-KV and shuffled-KV controls remain near chance.

## Why it stopped

No-paper closure: the Tier 1 mechanism is supported, but the evidence is synthetic and purpose-built rather than a pretrained-LM native KV intervention.

## Recommended next action

Run a bounded deepen test on a frozen GPT-2-small-class decoder using real native KV-cache or adapter-injected KV slots for the same anchor/log-count task, with serialized-context, no-KV, shuffled-KV, and parameter-matched controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen GPT-2-small Native KV Intervention for Anchor and Log-Count Recall
- Success threshold: At least 90% exact value accuracy and at least 80% log-count accuracy with correct KV, at least 5x relative improvement over serialized-context/no-KV baselines, and shuffled-KV mixed-task accuracy below 20%.
- Stop condition: Stop as unsupported if correct-KV accuracy is below 50% after a working implementation and reasonable prompt/adapter calibration, or if shuffled-KV performs within 10 percentage points of correct-KV.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-direct-kv-intervention-for-exact-anchors-plus-log-98b1dc3c48`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
