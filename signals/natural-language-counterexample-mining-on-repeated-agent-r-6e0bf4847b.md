# Natural-language counterexample mining on repeated-agent replay traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-counterexample-mining-on-repeated-agent-r-6e0bf4847b`
Run ID: `natural-language-counterexample-mining-on-repeated-agent-r-6e0bf4847b-20260613T011052081949+0000`

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

- Parent run decision: Counterexample Mining Loop for Agent Self-Correction: enoch://control-plane/projects/counterexample-mining-loop-for-agent-self-correction-337f34e0d547/runs/counterexample-mining-loop-for-agent-self-correction-337f34e0d547-20260613T002002009909+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce43259ae602

## What looked useful

Natural-language normalization appears to be a practical mechanism for mining counterexamples in repeated-agent replay traces when claims can be normalized to stable slots; exact string matching missed most paraphrased contradictions.

## Boundaries and scale limits

Synthetic controlled traces only; five slot families; deterministic templates and aliases; no real operator data, LLM-generated noisy replays, blind human labels, adversarial negation, temporal qualifiers, or large-schema memory.

## Claim scope

In a seeded Tier-1 controlled synthetic replay test with 40 planted contradiction traces and 40 matched controls, a deterministic natural-language slot/value normalizer mined repeated-agent counterexamples with F1 1.000 and false-positive rate 0.000, outperforming an exact-string baseline by 0.778 F1.

## Why it stopped

Tier-1 controlled direct threshold was met, but evidence is synthetic and schema-limited, so this is useful no-paper mechanism evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on LLM-generated repeated-agent replay traces with blind labels, negation/temporal cases, and the same exact-string baseline before any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-generated noisy replay counterexample mining with blind labels
- Success threshold: NL miner F1 >= 0.75, false-positive rate <= 0.20, and F1 gain over exact-string baseline >= 0.20 on blind-labeled noisy traces.
- Stop condition: Stop if F1 < 0.60, false-positive rate > 0.30, or errors are dominated by ambiguity requiring external human/private context rather than trace-local counterexamples.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-counterexample-mining-on-repeated-agent-r-6e0bf4847b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
