# Evidence-ledger halt for small CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-halt-for-small-cpu-agents-526ccfbf8f34`
Run ID: `evidence-ledger-halt-for-small-cpu-agents-526ccfbf8f34-20260608T093810873598+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1b9c9a573847

## What looked useful

Tracking independent evidence sources and requiring at least two independent supporting sources before answer halt prevented premature high-confidence answers caused by duplicate/correlated evidence in the local simulator. The tradeoff was higher evidence acquisition cost.

## Boundaries and scale limits

The evidence is synthetic and mechanism-isolating only. It does not validate real LLM agents, real retrieval corpora, calibrated model confidences, production tool traces, or user-facing factuality. Main run was 20,000 trials per synthetic condition on one CPU worker.

## Claim scope

In a seeded synthetic binary evidence-acquisition benchmark with source IDs and correlated/adversarial duplicate evidence, an evidence-ledger halt rule eliminated unsupported answers and improved accuracy versus posterior-confidence-only halting, at roughly 2.0x to 2.37x evidence steps versus confidence-only halting in duplicate-heavy conditions.

## Why it stopped

Synthetic/proxy evidence supports the halt mechanism but is not direct/full validation for real small CPU agents, so this is not paper-ready.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, test the same ledger halt rule on a small real retrieval-agent benchmark with source IDs and correctness labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real retrieval-agent evidence-ledger halt benchmark
- Success threshold: Ledger halt reduces unsupported or wrong answers by at least 20% relative to confidence-only halting in the duplicate/correlated-source condition, with no more than 2.5x average retrieval/tool steps and no regression larger than 3 percentage points in the independent-source control.
- Stop condition: Stop if real-agent ledger halting fails to reduce unsupported or wrong answers by at least 10% in the duplicate/correlated-source condition or requires more than 2.5x average retrieval/tool steps.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-halt-for-small-cpu-agents-526ccfbf8f34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
