# Direct Small-LLM Tool-Agent Evidence-Ledger Evaluation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-small-llm-tool-agent-evidence-ledger-evaluation-0adc836293`
Run ID: `direct-small-llm-tool-agent-evidence-ledger-evaluation-0adc836293-20260621T222531808798+0000`

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

- Parent run decision: Evidence-Ledger Agent with Counterexample Logging for Safer Small Agents: enoch://control-plane/projects/evidence-ledger-agent-with-counterexample-logging-for-safer-small-agents-db21cf302f51/runs/evidence-ledger-agent-with-counterexample-logging-for-safer-small-agents-db21cf302f51-20260621T220712206812+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf76d8b746b8

## What looked useful

Evidence-ledger prompting produced more complete tool chains on several tasks (notably t03, t07, t08) and improved accuracy by 16.7 percentage points after conservative rescoring, but the agent still failed 7/12 ledger tasks and did not solve harder chained relation queries.

## Boundaries and scale limits

Single small quantized model, one synthetic lookup environment, 12 tasks, CPU llama.cpp inference because the available build reported no usable GPU offload; no multi-model, naturalistic, or statistical robustness validation.

## Claim scope

On a 12-task synthetic multi-hop lookup benchmark using Phi-4-mini-instruct-Q4_K_M through llama.cpp, an explicit evidence-ledger prompt improved conservative answer accuracy from 3/12 to 5/12 versus a no-ledger tool-agent prompt, while increasing average steps and latency.

## Why it stopped

Tier 1 direct test produced a useful but non-paper-positive signal; it is not a full validation and the local llama.cpp build could not use GPU offload.

## Recommended next action

Run a medium confirmation with a GPU-enabled persistent server, at least 50 generated-but-auditable tasks, 2-3 small instruction models, and the same conservative scorer; stop if ledger delta is below +10 accuracy points or failures remain dominated by hallucinated tool arguments.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium multi-model evidence-ledger tool-agent confirmation
- Success threshold: Ledger accuracy exceeds baseline by >=10 percentage points on each evaluated model or by >=15 points pooled, with <=5% invalid JSON/action outputs and documented overhead.
- Stop condition: Stop as unsupported if ledger delta is <10 points on the first two models, if failures are mostly hallucinated arguments unaffected by ledgering, or if runtime exceeds the calibrated local budget without GPU offload.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-llm-tool-agent-evidence-ledger-evaluation-0adc836293`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
