# FSM Constrained Decoding for Tiny Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fsm-constrained-decoding-for-tiny-agents-0f7bedacaa53`
Run ID: `fsm-constrained-decoding-for-tiny-agents-0f7bedacaa53-20260528T091416947302+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/093bcd84ab6e

## What looked useful

Across four held-out paraphrase sampled-decoding runs, FSM masking increased validity from mean 0.781 to 1.000 and exact match from mean 0.229 to 0.295, with mean decode overhead of 0.466 ms/example. The mechanism is useful for format reliability but insufficient as a standalone semantic accuracy method.

## Boundaries and scale limits

Tested only on a synthetic five-device home-control command language, character-level decoding, 55 valid commands, 600 held-out paraphrase prompts per seed, and four random seeds on one GB10 GPU. Not validated on pretrained LLM tokenizers, real tool catalogs, multi-turn agents, or production traces.

## Claim scope

In a synthetic tiny-agent command-language task, a global trie/FSM decoding mask guarantees schema-valid JSON commands and modestly improves sampled exact-match success for a small attention seq2seq model, but it does not solve valid-but-wrong action or argument selection.

## Why it stopped

No-paper useful signal: the bounded synthetic evidence supports FSM format control but also shows the core limitation that global constraints leave many valid-but-wrong tool calls; this is not a publication-grade validation.

## Recommended next action

Run a bounded follow-up comparing global FSM constraints against prompt-conditioned FSM constraints or semantic validators on the same synthetic task, then only scale to pretrained tokenizers if valid-but-wrong errors drop materially.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-conditioned FSM constraints for tiny-agent tool calls
- Success threshold: Prompt-conditioned FSM keeps validity at 1.000 and reduces valid-but-wrong errors by at least 30% versus global FSM without more than 2x the global-FSM latency.
- Stop condition: Stop if prompt-conditioned constraints fail to reduce valid-but-wrong errors by 15% on two seeds, or if latency exceeds 2x global-FSM latency before semantic gains appear.

## Evidence references

- Artifact root: `<local-path>/projects/fsm-constrained-decoding-for-tiny-agents-0f7bedacaa53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
