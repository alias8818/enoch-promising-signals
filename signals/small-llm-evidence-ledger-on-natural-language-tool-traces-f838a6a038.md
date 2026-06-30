# Small-LLM Evidence Ledger on Natural-Language Tool Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-llm-evidence-ledger-on-natural-language-tool-traces-f838a6a038`
Run ID: `small-llm-evidence-ledger-on-natural-language-tool-traces-f838a6a038-20260522T174853062931+0000`

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

- Parent run decision: Tool-Use Evidence Ledger for Small Agents: enoch://control-plane/projects/tool-use-evidence-ledger-for-small-agents-9a80a6d8f940/runs/tool-use-evidence-ledger-for-small-agents-9a80a6d8f940-20260522T173447912241+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/79d3f7dbc52f

## What looked useful

Strict JSON metrics were all zero because outputs were malformed. Tolerant content scoring showed answer content accuracy 0.9875 for both answer-only and ledger-supervised conditions; ledger supervision improved tool-id F1 from 0.0 to 1.0 and quote recall from 0.0 to 1.0.

## Boundaries and scale limits

Test used 200 train, 40 validation, and 80 held-out synthetic examples with one 77M-parameter model family and greedy unconstrained decoding. It did not test real production traces, larger schemas, adversarial trace distributions, larger models, or constrained structured-output decoding.

## Claim scope

In a controlled Tier 1 synthetic natural-language tool-trace task, ledger-form fine-tuning of cached google/flan-t5-small preserved answer-content accuracy and caused generated text to include the correct evidence tool IDs and evidence phrases, but unconstrained decoding failed to produce strict valid JSON ledgers.

## Why it stopped

Closed as no-paper useful signal: the mechanism is supported under tolerant content scoring, but the strict machine-parseable ledger threshold failed under unconstrained decoding.

## Recommended next action

Run a bounded deepen follow-up with constrained JSON decoding or deterministic JSON repair, and require at least 95% strict JSON validity plus at least 0.90 evidence tool-id F1 on held-out controlled traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained JSON Evidence Ledgers for Small-LLM Tool Traces
- Success threshold: On at least 80 held-out controlled traces, strict JSON validity >= 0.95, evidence tool-id F1 >= 0.90, quote recall >= 0.90, and answer-content accuracy no more than 0.05 below the answer-only baseline.
- Stop condition: Stop if strict JSON validity remains below 0.80 or evidence tool-id F1 drops below 0.70 after constrained decoding or repair on the held-out set.

## Evidence references

- Artifact root: `<local-path>/projects/small-llm-evidence-ledger-on-natural-language-tool-traces-f838a6a038`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
