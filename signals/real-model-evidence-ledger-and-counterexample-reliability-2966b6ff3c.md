# Real-model evidence-ledger and counterexample reliability probe

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-evidence-ledger-and-counterexample-reliability-2966b6ff3c`
Run ID: `real-model-evidence-ledger-and-counterexample-reliability-2966b6ff3c-20260605T170453771024+0000`

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

- Parent run decision: Agent reliability via evidence ledger and counterexample logging: enoch://control-plane/projects/agent-reliability-via-evidence-ledger-and-counterexample-logging-ae41fb8055d7/runs/agent-reliability-via-evidence-ledger-and-counterexample-logging-ae41fb8055d7-20260605T134308662334+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/4be1fc6fa736

## What looked useful

The ledger prompt did not meet the pre-registered counterexample reliability threshold on either model. Qwen3-0.6B worsened false-counterexample reliability from 0.125 to 0.000. Qwen2.5-3B-Instruct improved strict-format and abstention behavior, but lenient rescoring showed no false-counterexample reliability gain: both direct and ledger were 0.500.

## Boundaries and scale limits

Small controlled arithmetic/logical suite; no natural-language evidence corpora, no persistent external ledger, no tool-assisted exhaustive search, and only two local instruction models.

## Claim scope

Prompt-only evidence-ledger prompting was tested against direct prompting on 16 verifier-backed integer universal claims using Qwen3-0.6B and Qwen2.5-3B-Instruct local inference.

## Why it stopped

Tier 1 real-model direct test failed the pre-registered +0.20 absolute false-counterexample reliability threshold; result is a small direct falsification of the prompt-only ledger mechanism, not a full validation of all ledger designs.

## Recommended next action

Do not write a paper from this run; run one bounded deepen test with a tool-enforced enumeration ledger before spending larger scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tool-enforced enumeration ledger for counterexample reliability
- Success threshold: Tool-enforced ledger false-counterexample reliability >= direct + 0.20 absolute and true-abstention reliability no more than 0.10 below direct.
- Stop condition: Stop if the tool-enforced ledger fails to beat direct false-counterexample reliability by at least 0.10 absolute on the first 25 balanced claims or if gains come only from abstention/formatting rather than valid counterexamples.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-evidence-ledger-and-counterexample-reliability-2966b6ff3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
