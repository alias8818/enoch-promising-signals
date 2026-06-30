# Real-LLM evidence-ledger gate on distractor tool-use tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-llm-evidence-ledger-gate-on-distractor-tool-use-tasks-4169268e1c`
Run ID: `real-llm-evidence-ledger-gate-on-distractor-tool-use-tasks-4169268e1c-20260607T124908457234+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Tiny agent evidence ledger reduces ungrounded tool use: enoch://control-plane/projects/tiny-agent-evidence-ledger-reduces-ungrounded-tool-use-0053ed7547d6/runs/tiny-agent-evidence-ledger-reduces-ungrounded-tool-use-0053ed7547d6-20260607T091733344571+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed5c7ff6fa8c

## What looked useful

The prompt-only evidence-ledger gate failed the Tier-1 threshold: aggregate distractor false-call rate stayed at 30% for baseline and ledger, while needed-tool accuracy dropped from 100% to 75%.

## Boundaries and scale limits

Only two local quantized instruct models were tested; no hosted frontier models, real tool execution, multi-turn agents, runtime validators, or larger benchmark suites were tested.

## Claim scope

In a deterministic 16-task controlled tool-planning suite on two local instruct GGUF LLMs, a prompt-only evidence-ledger gate did not reduce distractor tool-call proposals and reduced needed-tool recall for one model.

## Why it stopped

Direct Tier-1 threshold falsified: zero relative reduction in distractor false tool calls and a 25-point aggregate drop in needed-tool recall.

## Recommended next action

Stop this prompt-only gate as unsupported; a future bounded deepen test should replace the prompt-only instruction with an external validator that rejects unsupported tool calls before model/tool execution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Runtime ledger validator for distractor tool-use suppression
- Success threshold: At least 50% relative reduction in distractor false tool calls versus baseline and no more than 10 percentage-point reduction in needed-tool recall across both models.
- Stop condition: Stop if the validator cannot improve distractor false-call rate on the original 16-task suite or if needed-tool recall drops by more than 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-evidence-ledger-gate-on-distractor-tool-use-tasks-4169268e1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
